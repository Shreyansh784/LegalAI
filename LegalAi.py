# -*- coding: utf-8 -*-
"""LegalAI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1mUtZK0EMJ6QtHZ4uHe24Y8avDTgxdOiy
"""

!pip install transformers accelerate torch bitsandbytes

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model_name = "axondendriteplus/contract_drafter-Llama-3.2-1B-Instruct"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
).to("cuda")  # Ensure the model is on GPU

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "axondendriteplus/contract_drafter-Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
).to("cuda")  # Ensure the model is on GPU

# Gather user inputs
print("Please enter the following details for the Employment Agreement:")
company_name = input("Employer Company Name: ")
employee_name = input("Employee Name: ")
employee_address = input("Employee Address: ")
contact_number = input("Employee Contact Number: ")
employee_email = input("Employee Email: ")
employer_address = input("Employer Address: ")
employer_phone = input("Employer Phone: ")
employer_email = input("Employer Email: ")
start_date = input("Employment Start Date: ")
end_date = input("Employment End Date: ")
salary = input("Monthly Salary (in ₹): ")

# Construct the prompt with the user inputs
prompt = (
    f"Generate an Indian legal contract for: Employment Agreement between {company_name} and {employee_name}.\n\n"
    f"**Employee Details:**\n"
    f"Name: {employee_name}\n"
    f"Address: {employee_address}\n"
    f"Contact Number: {contact_number}\n"
    f"Email: {employee_email}\n\n"
    f"**Employer's Details:**\n"
    f"Company Name: {company_name}\n"
    f"Address: {employer_address}\n"
    f"Phone: {employer_phone}\n"
    f"Email: {employer_email}\n\n"
    f"**Terms & Conditions:**\n"
    f"The Employee agrees to work as a part-time/full-time employee with {company_name} starting from {start_date} until {end_date}. "
    f"Salary per month: ₹{salary}/- plus additional allowances as per company policies.\n\n"
    f"Please generate the complete legal contract in a detailed, formatted manner similar to a formal Indian Employment Agreement template."
)

# Tokenize input and move to GPU
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=2048,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

# Decode output
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nGenerated Employment Contract:\n")
print(response)

# Save the contract to a text file
with open("employment_agreement.txt", "w") as f:
    f.write(response)

print("\nContract saved as employment_agreement.txt")

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "axondendriteplus/contract_drafter-Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
).to("cuda")  # Ensure the model is on GPU

# Gather user inputs for the Lease Agreement
print("Please enter the following details for the Lease Agreement:")

landlord_name = input("Landlord Name: ")
landlord_address = input("Landlord Address: ")
landlord_contact = input("Landlord Contact Number: ")
landlord_email = input("Landlord Email: ")

tenant_name = input("Tenant Name: ")
tenant_address = input("Tenant Address: ")
tenant_contact = input("Tenant Contact Number: ")
tenant_email = input("Tenant Email: ")

property_address = input("Property Address: ")
lease_start_date = input("Lease Start Date: ")
lease_end_date = input("Lease End Date: ")
monthly_rent = input("Monthly Rent (in ₹): ")
security_deposit = input("Security Deposit (in ₹): ")

# Construct the prompt with the user inputs
prompt = (
    f"Generate an Indian legal contract for: Lease Agreement between {landlord_name} (Landlord) and {tenant_name} (Tenant).\n\n"
    f"**Landlord Details:**\n"
    f"Name: {landlord_name}\n"
    f"Address: {landlord_address}\n"
    f"Contact Number: {landlord_contact}\n"
    f"Email: {landlord_email}\n\n"
    f"**Tenant Details:**\n"
    f"Name: {tenant_name}\n"
    f"Address: {tenant_address}\n"
    f"Contact Number: {tenant_contact}\n"
    f"Email: {tenant_email}\n\n"
    f"**Property Details:**\n"
    f"Property Address: {property_address}\n\n"
    f"**Lease Terms:**\n"
    f"Lease Period: From {lease_start_date} to {lease_end_date}\n"
    f"Monthly Rent: ₹{monthly_rent}\n"
    f"Security Deposit: ₹{security_deposit}\n\n"
    f"Please generate a complete and detailed legal lease agreement formatted as a formal Indian Lease Agreement template, including all essential clauses such as payment terms, maintenance responsibilities, termination conditions, and dispute resolution."
)

# Tokenize input and move to GPU
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=2048,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

# Decode output
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nGenerated Lease Agreement:\n")
print(response)

# Save the contract to a text file
with open("lease_agreement.txt", "w") as f:
    f.write(response)

print("\nContract saved as lease_agreement.txt")

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_name = "axondendriteplus/contract_drafter-Llama-3.2-1B-Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto"
).to("cuda")  # Ensure the model is on GPU

# Gather user inputs for Business Agreement
print("Please enter the following details for the Business Agreement:")

company_name = input("Company Name: ")
company_address = input("Company Address: ")
partner_name = input("Partner Name: ")
partner_address = input("Partner Address: ")
service_description = input("Scope of Work and Services: ")
payment_terms = input("Payment Terms: ")
agreement_duration = input("Agreement Duration: ")
dispute_resolution = input("Dispute Resolution Method: ")
termination_clause = input("Termination Clause: ")

# Construct the prompt with user inputs
prompt = (
    f"Generate an Indian legal contract for: Business Agreement.\n\n"
    f"**Company Details:**\n"
    f"Company Name: {company_name}\n"
    f"Address: {company_address}\n\n"
    f"**Parties Involved:**\n"
    f"1. {company_name}, hereinafter referred to as 'The Company'\n"
    f"   - Registered at: {company_address}\n\n"
    f"2. {partner_name}, hereinafter referred to as 'Partner'\n"
    f"   - Partner Address: {partner_address}\n\n"
    f"**Scope of Work and Services:** {service_description}\n\n"
    f"**Payment Terms:** {payment_terms}\n\n"
    f"**Agreement Duration:** {agreement_duration}\n\n"
    f"**Dispute Resolution:** {dispute_resolution}\n\n"
    f"**Termination Clause:** {termination_clause}\n\n"
    f"Please generate a complete and detailed Indian Business Agreement, including essential clauses such as obligations, liabilities, confidentiality, force majeure, governing law, and termination conditions."
)

# Tokenize input and move to GPU
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

# Generate response
outputs = model.generate(
    **inputs,
    max_new_tokens=2048,
    temperature=0.7,
    top_p=0.95,
    repetition_penalty=1.15
)

# Decode output
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("\nGenerated Business Agreement:\n")
print(response)

# Save the contract to a text file
with open("business_agreement.txt", "w") as f:
    f.write(response)

print("\nContract saved as business_agreement.txt")

!pip install fpdf

from fpdf import FPDF

def text_to_pdf(input_text_file, output_pdf_file):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    with open(input_text_file, "r", encoding="utf-8") as file:
        for line in file:
            line = line.replace("₹", "INR")  # Fix Rupee symbol
            line = line.replace("’", "'")   # Fix curly apostrophe
            line = line.replace("“", '"').replace("”", '"')  # Fix curly quotes

            pdf.multi_cell(0, 10, txt=line.strip(), align="L")  # Use multi_cell to handle long lines

    pdf.output(output_pdf_file)
    print(f"PDF saved as {output_pdf_file}")

# Convert text file to PDF
input_text_file = "lease_agreement.txt"
output_pdf_file = "lease_contract.pdf"
text_to_pdf(input_text_file, output_pdf_file)

!pip install googletrans==4.0.0-rc1

from googletrans import Translator

def translate_text_file(input_file, output_file, dest_lang="hi"):
    translator = Translator()

    # Read the English text file
    with open(input_file, "r", encoding="utf-8") as file:
        english_text = file.read()

    # Translate to Hindi
    translated_text = translator.translate(english_text, dest=dest_lang).text

    # Save the Hindi text to a new file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(translated_text)

    print(f"Translation completed! Hindi text saved in: {output_file}")

# Example usage
input_file = "/content/employment_agreement.txt"  # Replace with your text file
output_file = "hindi_employment_agreement.txt"
translate_text_file(input_file, output_file)

!pip install reportlab

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def text_to_pdf(input_text_file, output_pdf_file):
    c = canvas.Canvas(output_pdf_file, pagesize=letter)
    c.setFont("Helvetica", 12)

    with open(input_text_file, "r", encoding="utf-8") as file:
        y = 750  # Start position for text
        for line in file:
            c.drawString(100, y, line.strip())
            y -= 20  # Move down for the next line

    c.save()
    print(f"PDF saved as {output_pdf_file}")

# Convert Hindi text file to PDF
text_to_pdf("/content/hindi_lease_agreement.txt", "hindi_lease_agreement.pdf")