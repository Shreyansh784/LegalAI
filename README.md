# 🤝 AI-Generated Legal Drafts and Contracts

A Generative AI system that helps businesses and legal professionals draft customized contracts and legal documents based on user-defined clauses and inputs.

---

## ✨ Overview

This project is a Generative AI-based legal document generator that dynamically creates legally structured contracts based on user inputs. Unlike traditional template-based tools, it leverages Large Language Models (LLMs) to tailor each document to specific needs.

Supported contract types include:
- Employment Agreements
- Business Contracts
- Non-Disclosure Agreements (NDAs)
- Rental/Lease Agreements
- And more...

Users input relevant details like party names, scope of work, compensation, and timeline. The AI then outputs a complete, formatted legal document with standard and user-defined clauses such as confidentiality, dispute resolution, and termination.

The system is designed for GPU-accelerated environments (Google Colab, AWS, etc.) to handle the high computational load of LLM-based text generation.

---

## 🌟 Key Features

- **📄 Dynamic Contract Generation**: Each document is uniquely crafted based on user input.
- **⚖️ Clause Customization**: Add or edit clauses like confidentiality, liability, and more.
- **⚡ GPU Accelerated**: Efficient generation using CUDA-enabled environments.
- **🌐 Multilingual (Hindi Translation)**: Translate contracts into Hindi with support for more languages coming soon.
- **🌐 PDF Export**: Export contracts as professionally formatted PDFs.
- **⚛️ Extensible**: Easily add support for new contract types or jurisdictions.

---

## 🛠️ Tech Stack

### Frontend (Optional)
- **Next.js**: React framework for building an interactive interface.
- **TypeScript**: Type-safe development for reliability.
- **Prisma ORM + PostgreSQL**: Backend support for contract logs or user data.
- **tRPC**: Type-safe client-server communication.

### AI Backend
- **Hugging Face Transformers**: Used for inference with custom legal LLM.
- **Model**: [`axondendriteplus/contract_drafter-Llama-3.2-1B-Instruct`](https://huggingface.co/axondendriteplus/contract_drafter-Llama-3.2-1B-Instruct)
- **Torch + Accelerate + BitsAndBytes**: For efficient model execution.
- **Google Colab / CUDA Environment**: Recommended for GPU inference.
- **Googletrans**: For translation support.
- **FPDF & ReportLab**: For PDF generation from text.

---

## 🚫 Challenges Faced

- **🚀 GPU Limitations**: Large models need expensive computational resources.
- **📅 Legal Precision**: LLMs may not always produce jurisdiction-specific or legally binding content.
- **🔍 Dataset Scarcity**: No labeled legal dataset used; relies on prompt engineering.

---

## 🤖 Future Improvements

- **Multilingual Support**: Expand to regional and international languages.
- **Legal Compliance Checkers**: Integration with compliance APIs or legal databases.
- **Web Dashboard**: Upload & manage generated contracts with a user-friendly UI.
- **Clause Template Library**: Predefined clauses that users can insert/edit easily.

---

## ⚙️ How It Works

1. **User Inputs**: Prompted for key contract details (names, duration, payment, etc.)
2. **Prompt Template**: Data is formatted into a structured prompt.
3. **LLM Generation**: Model generates a complete contract using legal tone.
4. **Review/Export**: Contract is printed, saved as `.txt`, and exported as `.pdf`.
5. **Translation (Optional)**: Contract translated into Hindi (or other languages).

---


---

## ⚡ Usage Instructions

1. Run the notebook in a GPU-enabled environment (like Google Colab).

2. Input contract details when prompted.

3. Contract will be generated, saved, translated (if enabled), and exported to PDF.

---

## 📄 License

This project is licensed under the MIT License. You are free to use, modify, and distribute it with attribution.

---

Built with ❤️ for simplifying legal automation in India and beyond.

