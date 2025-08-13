issue title: Rails Workflow Generator
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/278
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 1, there's a Rails generator for creating new workflows mentioned.

## Feature Details
The book mentions:
"Rails: First-class Rails integration with generators and conventions. Run `rails generate roast:workflow ProductDescription` and you're ready to go"

This generator should create:
```bash
rails generate roast:workflow ProductDescription

# Creates:
# app/workflows/product_description_workflow.rb
# app/roast/product_description/
# spec/workflows/product_description_workflow_spec.rb
```

## Generated Workflow Template
```ruby
# app/workflows/product_description_workflow.rb
class ProductDescriptionWorkflow < ApplicationWorkflow
  def execute
    step :analyze_product do
      prompt <<~PROMPT
        Analyze the following product and extract key features:
        #{params[:product].attributes.to_json}
      PROMPT
    end
    
    step :generate_description do
      prompt template: "product_description/generate_description"
      context previous_analysis: previous_step.output
    end
    
    output description: current_step.output[:description]
  end
end
```

## Generated Test Template
```ruby
# spec/workflows/product_description_workflow_spec.rb
require 'rails_helper'

RSpec.describe ProductDescriptionWorkflow do
  let(:product) { create(:product) }
  let(:workflow) { described_class.new(product: product) }
  
  describe '#execute' do
    it 'generates a product description' do
      stub_roast_response(
        workflow: 'ProductDescriptionWorkflow',
        step: 'generate_description',
        response: { description: 'Test description' }
      )
      
      result = workflow.execute
      
      expect(result.success?).to be true
      expect(result.output[:description]).to be_present
    end
  end
end
```

## Rationale
Rails developers expect generators for creating new components. This speeds up development and ensures consistent structure.

## Acceptance Criteria
- [ ] Generator creates workflow class with proper inheritance
- [ ] Creates directory structure for prompts
- [ ] Generates test file (RSpec or Minitest based on app config)
- [ ] Follows Rails naming conventions
- [ ] Supports options like --skip-test
- [ ] Clear output showing created files

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
