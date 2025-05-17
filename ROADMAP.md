# AgentAmi - Roadmap
This file is a roadmap for the future features which I might implement:

1. Advanced Pruning Strategies: Exposing multiple pruning strategies to select for better token size optimization for different use cases.
2. Ability to give user to write their own pruner.
3. Option for user to select from various tool_selectors, which will be natively implemented.

	
Few immediate features and bugs that need to be addressed:
1) Pruner is pruning without considering the message is a Tool message or AI message, it needs to look into what is permissible.
2) option to disable tool_selector altogether.
