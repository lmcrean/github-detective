issue title: Limit tool output size
labels: enhancement
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/52
status: open
date opened: 2025-05-17
repo 30d_merge_rate: 13

====

description:
Sometimes a tool will output a lot of text and break the context window limit.
```
🔧 Running command: ls -R .
Chat completion failed!!!!!!!!!!!!!!!!: {"error" => {"message" => "Invalid 'messages[5].content': string too long. Expected a string with maximum length 10485760, but got a string with length 10605342 instead.", "type" => "invalid_request_error", "param" => "messages[5].content", "code" => "string_above_max_length"}}
```

===
