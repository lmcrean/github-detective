issue title: RSpec and Minitest Integration for Testing Workflows
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/275
status: open
date opened: 2025-06-18
repo 30d_merge_rate: 13

====

description:
## Description
From "The Roast Book" Chapter 1, Roast is described as having "Full RSpec and Minitest support with deterministic test helpers."

## Feature Details
The book mentions test helpers like `stub_roast_response` for predictable testing:

```ruby
# RSpec example
RSpec.describe ArticleSummaryWorkflow do
  it "generates a summary" do
    stub_roast_response(
      workflow: "ArticleSummaryWorkflow",
      step: "summarize",
      response: { summary: "Test summary" }
    )
    
    workflow = ArticleSummaryWorkflow.new(article: article)
    result = workflow.execute
    
    expect(result.output[:summary]).to eq("Test summary")
  end
end

# Minitest example
class ArticleSummaryWorkflowTest < ActiveSupport::TestCase
  test "generates a summary" do
    stub_roast_response(
      workflow: "ArticleSummaryWorkflow",
      step: "summarize",
      response: { summary: "Test summary" }
    )
    
    workflow = ArticleSummaryWorkflow.new(article: article)
    result = workflow.execute
    
    assert_equal "Test summary", result.output[:summary]
  end
end
```

## Test Helpers Needed
1. `stub_roast_response` - Stub specific workflow/step responses
2. `stub_all_roast_responses` - Stub all AI calls
3. `assert_roast_called` - Verify workflow was executed
4. `with_roast_recording` - Record/replay pattern for tests

## Rationale
Testing AI workflows requires deterministic responses. Rails developers expect good test helpers for both RSpec and Minitest.

## Acceptance Criteria
- [ ] RSpec support file with helpers and matchers
- [ ] Minitest support with assertions
- [ ] Deterministic response stubbing
- [ ] VCR-like recording/replay for AI responses
- [ ] Clear documentation with testing examples
- [ ] Support for testing specific steps in isolation
- [ ] Test mode that prevents real API calls

## Note
This feature is described in "The Roast Book" as an existing capability but doesn't currently exist in the codebase.

===
