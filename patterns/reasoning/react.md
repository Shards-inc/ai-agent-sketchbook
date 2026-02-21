# ReAct: Synergizing Reasoning and Acting

**ReAct** is a paradigm that combines reasoning (Chain-of-Thought) with acting (Tool Use) in a seamless loop.

## 🧠 Concept

In the ReAct pattern, the agent generates a "Thought" about the current state, takes an "Action" (like searching the web or calling an API), and then receives an "Observation" from the environment. This cycle continues until the task is complete.

## 🔄 The ReAct Loop

1. **Thought**: "I need to find the current price of Bitcoin to answer the user's question."
2. **Action**: `get_crypto_price(symbol="BTC")`
3. **Observation**: `{"price": "52000.00", "currency": "USD"}`
4. **Thought**: "The price is $52,000. I can now answer the user."
5. **Final Answer**: "The current price of Bitcoin is $52,000 USD."

## 📚 Resources

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
