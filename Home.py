"""
LLM Bootcamp Project - Home Page
Landing page for the AI chatbot platform with multiple capabilities.
"""

import streamlit as st

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(
    page_title="Project Astra",
    page_icon="🤖",
    layout="wide"
)

# ============================================================================
# MAIN CONTENT
# ============================================================================

st.title("🤖 Project Astra")
st.write("Explore AI chatbot with multiple capabilities")

st.subheader("Available AI Assistants:")

# List of available features
st.write("💬 **Basic AI Chat** - Simple AI conversation")
st.write("🔍 **Search Enabled Chat** - AI with internet search capabilities")
st.write("📚 **RAG** - Retrieval-Augmented Generation with documents")
st.write("🔧 **MCP Chatbot** - Model Context Protocol integration")
