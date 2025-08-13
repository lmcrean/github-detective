issue title: Feature Request: Add Ollama LLM Support via `ollama-ai` Gem
labels: none
comment count: 0
hyperlink: https://github.com/shopify/roast/issues/288
status: open
date opened: 2025-06-20
repo 30d_merge_rate: 13

====

description:
### Is your feature request related to a problem? Please describe.

Currently, Roast primarily integrates with cloud-based LLM providers like OpenAI and OpenRouter. This limits users who prefer to run LLMs locally for privacy, cost efficiency, or specific hardware utilization. Integrating Ollama would provide a powerful option for local and self-hosted model execution within Roast workflows.

### Describe the solution you'd like

I propose adding support for Ollama LLMs within the Roast framework. This can be effectively achieved by leveraging the existing Ruby client library, [`ollama-ai` Gem](https://github.com/gbaptista/ollama-ai).

The integration would involve:

1.  **Introducing a new `Ollama` provider**: Similar to how existing providers (e.g., OpenAI) are handled, a new abstraction for Ollama would be created.
2.  **Utilizing `ollama-ai` Gem**: This gem provides a robust and easy-to-use interface for interacting with the Ollama API, handling requests for completions, chat, and potentially embeddings.
3.  **Configuration**: Allow users to specify Ollama models in their Roast YAML workflow definitions (e.g., `model: ollama/llama2`).
4.  **Local Execution**: Enable Roast to seamlessly connect to a locally running Ollama instance, supporting various models downloaded via Ollama.

### Describe alternatives you've considered

* **Manual HTTP requests**: Directly implementing HTTP requests to the Ollama API without a gem. While feasible, this would involve reimplementing API client logic already provided by `ollama-ai`, leading to more maintenance overhead.
* **Other Ruby Ollama gems**: While `ollama-ruby` exists, `ollama-ai` appears to be actively maintained and covers a comprehensive set of Ollama API functionalities. `langchainrb` and `RubyLLM` are higher-level frameworks that might be an option if Roast aims for a more abstract LLM integration layer. However, `ollama-ai` is a more direct client.

### Additional context

Integrating Ollama would significantly expand Roast's versatility by offering a powerful open-source, local LLM option. This aligns with the growing trend of running LLMs on personal hardware and would make Roast an even more attractive framework for a wider range of AI workflow developers.

I am happy to contribute to the implementation or provide further assistance if this feature is considered.

===
