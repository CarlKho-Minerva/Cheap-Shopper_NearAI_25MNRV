# Shop Cheap

**Find the lowest-priced products on Google Shopping with AI-powered suggestions**

## Overview

Shop Cheap is an AI shopping assistant built on NEAR AI that helps users find the absolute lowest prices on products across Google Shopping. With a clean, distraction-free interface and intelligent feature suggestions, Shop Cheap streamlines the online shopping experience.

[![Live Demo](https://img.shields.io/badge/Live_Demo-Try_It_Now-blue)](https://chat.near.ai/agents/carlkho.near/shop-cheap/latest)
[![NEAR AI](https://img.shields.io/badge/Built_on-NEAR_AI-green)](https://app.near.ai/agents/carlkho.near/shop-cheap/latest)
[![GitHub URL](https://img.shields.io/badge/View-GitHub_Repo-white)](https://github.com/CarlKho-Minerva/Cheap-Shopper_NearAI_25MNRV)

## Features

- ✅ Natural language product search
- ✅ Direct links to Google Shopping sorted from lowest to highest price
- ✅ Intelligent feature suggestions based on product type
- ✅ Clean, minimal interface focused on finding the best deals
- ✅ Works for any product category

## Architecture

Shop Cheap is built on NEAR AI's agent infrastructure with the following components:

```mermaid
flowchart TD
    A[User Interface\nNEAR Agent] <--> B[NEAR AI Platform\nAgent Environment]
    B <--> C[LLama-v3p1-70b\nFireworks AI]
    B --> D[Search Query\nOptimization]
    D <--> E[Google Shopping\nSearch Results]
    A --> E
```

## Installation & Setup

### Prerequisites

- NEAR AI account
- Basic knowledge of Python

### Steps to Deploy Your Own Version

1. **Create a NEAR AI Account**
   - Sign up at [app.near.ai](https://app.near.ai)

2. **Set Up Your Agent**
   - Navigate to the Agents section
   - Click "Create New Agent"
   - Follow the setup wizard

3. **Deploy the Code**
   - Copy the `run.py` file from this repository
   - Paste it into your agent's code editor
   - Update the metadata as needed

4. **Configure Settings**
   - Set the model to `llama-v3p1-70b-instruct`
   - Set provider to `fireworks`
   - Set temperature to `1.0`
   - Set max tokens to `16384`

5. **Deploy**
   - Click "Deploy" to make your agent live

## Cheap Shopper NearAI Benchmark Results

### Methodology

I conducted qualitative/quantitative user testing with three participants (Minjae, Jeevan, and Uliana) to evaluate the performance of our Cheap Shopper system. Each participant performed 5 different shopping queries, and we measured the following metrics:

1. **Query Understanding**: Whether the system correctly interpreted the user's query (binary: yes/no)
2. **Link Generation**: Whether appropriate shopping links were generated (binary: yes/no)
3. **Feature Relevance**: How relevant the suggested features were to the query (scale: 0-1)
4. **Response Time**: Time taken for the system to respond (in seconds)
5. **Task Completion**: Whether the user successfully completed their shopping task (binary: yes/no)

### Key Performance Metrics

![Key Performance Metrics](key_metrics.png)

As shown above, our system achieved:

- **Query Understanding**: 100% - Perfect understanding of all queries
- **Link Generation**: 100% - Successfully generated appropriate links for all queries
- **Feature Relevance**: 80.2% - Good but with room for improvement
- **Task Completion**: 100% - All users could complete their tasks via Google Shopping

### Response Time Analysis

![Response Time Analysis](response_time.png)

Despite efforts to optimize with a lower parameter model, our system's response time remains slower than desired, averaging around 5.7 seconds. This is an area identified for improvement in future iterations.

### Participant Comparison

![Participant Comparison](participant_comparison.png)

The radar chart shows how metrics were consistent across all participants, with feature relevance being the only metric below 100%.

### Conclusion

The benchmark tests confirm that our Cheap Shopper system excels at query understanding, link generation, and enabling task completion. Feature relevance, while good at 80%, has room for improvement. The main area requiring optimization is response time, as the current average of 5.7 seconds is slower than our target threshold despite using a lower parameter model.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Carl Kho - [LinkedIn](https://www.linkedin.com/in/carlkho/)

Project Link: <https://github.com/CarlKho-Minerva/Cheap-Shopper_NearAI_25MNRV>

## Acknowledgements

- [NEAR AI](https://near.ai) for providing the agent infrastructure
- [Fireworks AI](https://fireworks.ai) for the LLM model
- Silverstream AI for the hackathon bounty challenge
