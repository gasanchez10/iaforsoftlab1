# Definitions:

1. **Zero-shot Prompting**:
    A model is given a task with no prior examples or training data specific to that task.

2. **Few-shot Prompting**:
   A model is provided with a small number of examples to guide its performance on a specific task.

3. **Chain-of-Thought (CoT) Prompting**:
   The model is encouraged to generate a sequence of intermediate reasoning steps leading to the final answer, improving its performance on complex tasks.

4. **Self-Consistency**:
   Multiple reasoning paths are generated and the most consistent answer among them is selected as the final output.

5. **Generate Knowledge Prompting**:
   The model generates background knowledge or context before attempting to answer a question or solve a problem, improving its understanding and performance.

6. **Prompt Chaining**:
    A sequence of prompts where the output of one prompt is used as the input for the next, allowing for more complex interactions and refined outputs.

7. **Tree of Thoughts**:
   The model explores multiple potential solution paths (like branches of a tree) and evaluates them to find the most promising one.

8. **Retrieval Augmented Generation (RAG)**:
   Combines retrieval of relevant documents or information with generation, allowing the model to access and use external knowledge sources.

9. **Directional Stimulus Prompting**:
   Prompts are designed to guide the model's attention and responses in a specific direction, enhancing its focus and output quality.

10. **ReAct Prompting**:
    The model alternates between thinking through a problem and taking action based on its reasoning.

11. **Multimodal CoT Prompting**:
    Extends Chain-of-Thought prompting to include multiple modalities (e.g., text, images, audio), allowing the model to reason across different types of data.