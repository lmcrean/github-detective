issue title: Tapioca v0.17.2 fails to generate signature for `AbstractController::Collector#turbo_stream`
labels: help-wanted
comment count: 3
hyperlink: https://github.com/shopify/tapioca/issues/2334
status: open
date opened: 2025-06-24
repo 30d_merge_rate: 12

====

description:
After upgrading Tapioca to 0.17.2 (or more recent) and regenerating the RBI for actionpack, the signature for `AbstractController::Collector#turbo_stream` is missing.

The `AbstractController::Collector` methods are dynamically generated based on `Mime::SET`: https://github.com/rails/rails/blob/v8.0.2/actionpack/lib/abstract_controller/collector.rb#L18-L20

The turbo-rails gem registers the `turbo_stream` format in a Rails initializer: https://github.com/hotwired/turbo-rails/blob/v2.0.16/lib/turbo/engine.rb#L102-L104

So it looks like something changed in 0.17.2 that causes the Rails initializer to no longer be executed.

This is problematic for us because we have code in controllers like this:
```ruby
respond_to do |format|
  format.turbo_stream do
    render(turbo_stream: ...)
  end
end
```

and after regenerating the RBI for actionpack, the code above produces a Sorbet error:
```
Method `turbo_stream` does not exist on `ActionController::MimeResponds::Collector`
```

===

comment #1 by KaanOzkan, 2025-06-25, 17:35:45
Feels like it might be due to https://github.com/Shopify/tapioca/pull/293 but I think the dynamic generation would have the method's source location as `AbstractController::Collector`.

comment #2 by olivier-thatch, 2025-06-25, 19:33:49
That does seem to be the case:
```ruby
AbstractController::Collector.instance_method(:turbo_stream).source_location
# => ["/Users/olivier/.rbenv/versions/3.4.4/lib/ruby/gems/3.4.0/gems/actionpack-8.0.2/lib/abstract_controller/collector.rb", 12]
```

comment #3 by KaanOzkan, 2025-06-26, 13:45:51
Until this is investigated users can manually define the method using a [shim](https://github.com/Shopify/tapioca?tab=readme-ov-file#rbi-files-for-missing-constants-and-methods).
