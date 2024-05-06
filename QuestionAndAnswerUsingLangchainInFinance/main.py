from QnA import answer_question, generate_answer
import FAISS_INDEX  # Import your FAISS index update module
import streamlit as st
import json
import plotly.express as px


# Load metrics data from a JSON file
def load_metrics(filename='metrics.json'):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


# Plotting function using Plotly
def plot_metrics(metrics, metric_key, title):
    if isinstance(metrics, dict):
        values = list(metrics.values())
        labels = list(metrics.keys())
    else:
        values = [metrics]  # Assuming metrics might be a single numeric value
        labels = [metric_key]

    fig = px.bar(
        x=labels,
        y=values,
        labels={'x': 'Metric', 'y': 'Value'},
        title=title
    )
    return fig


# Streamlit UI setup
st.title("Question Answering System")

col1, col2 = st.columns(2)
with col1:
    question = st.text_input("Enter your question:")
with col2:
    engine_choice = st.radio("Choose your answering engine:", ('openai', 'hugging_face'))

if st.button('Get Answer'):
    if question:
        answer, source_url = answer_question(question, model_choice=engine_choice)
        st.text("Answer:")
        st.write(answer)
        if source_url:
            st.markdown(f"[Source URL]({source_url})", unsafe_allow_html=True)
    else:
        st.error("Please enter a question.")

with st.sidebar:
    st.write("## Show Metrics")
    all_data = load_metrics()
    selected_engine = st.selectbox("Select Engine", options=list(all_data.keys()), index=0)
    selected_metric = st.selectbox("Select Metric Type", options=['rouge', 'bleu', 'bert_score'], index=0)

    if st.button('Display Metrics'):
        metrics_data = all_data[selected_engine][selected_metric]
        if isinstance(metrics_data, dict):
            # Display metrics values as a table
            st.write(f"{selected_metric.upper()} Metrics for {selected_engine.capitalize()}:")
            st.json(metrics_data)  # This will format the dictionary nicely in the UI
        else:
            # Handle case where metrics data might not be a dictionary
            st.write(f"{selected_metric.upper()} Metric for {selected_engine.capitalize()}: {metrics_data}")

        # Plot and display the graph
        st.plotly_chart(plot_metrics(metrics_data, selected_metric, f"{selected_metric.upper()} Metrics"))

with st.sidebar:
    st.write("## Admin Actions")
    update_password = st.text_input("Enter password to update Vector DB:", type="password")
    if st.button('Update Vector DB'):
        if update_password == "5731_project":
            FAISS_INDEX.update_faiss_index()
            st.success("Vector DB Updated Successfully!")
        else:
            st.error("Incorrect password.")
