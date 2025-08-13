issue title: ActiveModelAttributes compiler does not allow calling "super" from attribute method overrides.
labels: none
comment count: 1
hyperlink: https://github.com/shopify/tapioca/issues/2307
status: open
date opened: 2025-06-03
repo 30d_merge_rate: 12

====

description:
Currently the `Tapioca::Dsl::Compilers::ActiveModelAttributes` compiler defines the attribute accessor methods directly on the model class:

```ruby
class GeneralLedgerController::Model
    sig { returns(T.nilable(::String)) }
    def classification; end

    sig { params(value: T.nilable(::String)).returns(T.nilable(::String)) }
    def classification=(value); end
end
```

But `ActiveModel` actually lets you call `super` on overridden attribute methods:

```ruby
class GeneralLedgerController::Model
  include ActiveModel::Attributes

  attribute :classification, :string

  def classification=(klass)
    super(klass + " something else")
  end
end
```

I believe this works because `ActiveModel::Attributes` actually defines the methods in an anonymous module which is included in the model class.

This causes Sorbet to fail to detect the `super` method. Would it be a good idea to update the compiler to define the attribute methods in a module? I've updated the compiler and included it in my project, simply wrapping the defined methods in a module and including it, and it seems to work:

```ruby
# typed: strict
# frozen_string_literal: true

return unless defined?(ActiveModel::Attributes)

require "tapioca/dsl/helpers/active_model_type_helper"

module Tapioca
  module Dsl
    module Compilers
      # `Tapioca::Dsl::Compilers::ActiveModelAttributes` decorates RBI files for all
      # classes that use [`ActiveModel::Attributes`](https://edgeapi.rubyonrails.org/classes/ActiveModel/Attributes/ClassMethods.html).
      #
      # For example, with the following class:
      #
      # ~~~rb
      # class Shop
      #   include ActiveModel::Attributes
      #
      #   attribute :name, :string
      # end
      # ~~~
      #
      # this compiler will produce an RBI file with the following content:
      # ~~~rbi
      # # typed: true
      #
      # class Shop
      #
      #   sig { returns(T.nilable(::String)) }
      #   def name; end
      #
      #   sig { params(name: T.nilable(::String)).returns(T.nilable(::String)) }
      #   def name=(name); end
      # end
      # ~~~
      class MojoActiveModelAttributes < Compiler
        extend T::Sig

        ConstantType = type_member do
          { fixed: T.all(T::Class[::ActiveModel::Attributes], ::ActiveModel::Attributes::ClassMethods) }
        end

        # @override
        #: -> void
        def decorate
          attribute_methods = attribute_methods_for_constant
          return if attribute_methods.empty?

          root.create_path(constant) do |klass|
            klass.create_module("ActiveModelAttributes") do |mod|
              attribute_methods.each do |method, attribute_type|
                generate_method(mod, method, attribute_type)
              end
            end
            klass.create_include("ActiveModelAttributes")
          end
        end

        class << self
          extend T::Sig

          # @override
          #: -> T::Enumerable[Module]
          def gather_constants
            all_classes.grep(::ActiveModel::Attributes::ClassMethods)
          end
        end

        private

        HANDLED_METHOD_TARGETS = ["attribute", "attribute="] #: Array[String]

        #: -> Array[[::String, ::String]]
        def attribute_methods_for_constant
          patterns = if constant.respond_to?(:attribute_method_patterns)
                       # https://github.com/rails/rails/pull/44367
                       constant.attribute_method_patterns
                     else
                       T.unsafe(constant).attribute_method_matchers
                     end
          patterns.flat_map do |pattern|
            constant.attribute_types.filter_map do |name, value|
              next unless handle_method_pattern?(pattern)

              [pattern.method_name(name), type_for(value)]
            end
          end
        end

        #: (untyped pattern) -> bool
        def handle_method_pattern?(pattern)
          target = if pattern.respond_to?(:method_missing_target)
                     # Pre-Rails 6.0, the field is named "method_missing_target"
                     T.unsafe(pattern).method_missing_target
                   elsif pattern.respond_to?(:target)
                     # Rails 6.0+ has renamed the field to "target"
                     pattern.target
                   else
                     # https://github.com/rails/rails/pull/44367/files
                     T.unsafe(pattern).proxy_target
                   end

          HANDLED_METHOD_TARGETS.include?(target.to_s)
        end

        #: (untyped attribute_type_value) -> ::String
        def type_for(attribute_type_value)
          case attribute_type_value
          when ActiveModel::Type::Boolean
            as_nilable_type("T::Boolean")
          when ActiveModel::Type::Date
            as_nilable_type("::Date")
          when ActiveModel::Type::DateTime, ActiveModel::Type::Time
            as_nilable_type("::Time")
          when ActiveModel::Type::Decimal
            as_nilable_type("::BigDecimal")
          when ActiveModel::Type::Float
            as_nilable_type("::Float")
          when ActiveModel::Type::Integer
            as_nilable_type("::Integer")
          when ActiveModel::Type::String
            as_nilable_type("::String")
          else
            type = Helpers::ActiveModelTypeHelper.type_for(attribute_type_value)
            type = as_nilable_type(type) if Helpers::ActiveModelTypeHelper.assume_nilable?(attribute_type_value)
            type
          end
        end

        #: (RBI::Scope klass, String method, String type) -> void
        def generate_method(klass, method, type)
          if method.end_with?("=")
            parameter = create_param("value", type: type)
            klass.create_method(
              method,
              parameters: [parameter],
              return_type: type
            )
          else
            klass.create_method(method, return_type: type)
          end
        end
      end
    end
  end
end
```

Does this have unintended consequences? I'm using a named module which might have a conflict, maybe generating an anonymous module would be better, I'm not sure how to do that with the Tapioca API

===

comment #1 by allcre, 2025-06-23, 14:11:48
Hello! This is a good update to the compiler, and using a named module is consistent with what other tapioca compilers already do, e.g. [smart_properties](https://github.com/Shopify/tapioca/blob/dfa8ebdd983048200de950a7a815e781ae08706e/lib/tapioca/dsl/compilers/smart_properties.rb), [url_hepers](https://github.com/Shopify/tapioca/blob/dfa8ebdd983048200de950a7a815e781ae08706e/lib/tapioca/dsl/compilers/url_helpers.rb), and [active_record_columns](https://github.com/Shopify/tapioca/blob/dfa8ebdd983048200de950a7a815e781ae08706e/lib/tapioca/dsl/compilers/active_record_columns.rb). Please open a PR with your changes and we will review.
