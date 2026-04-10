import streamlit as st
from g_structured_output_cls import extract_recipe
 
st.title("Recipe Extractor")
st.write("Paste a recipe description and extract its structured details.")
 
text_input = st.text_area("Recipe text", height=200,
placeholder="Describe your recipe here...")

if st.button("Extract Recipe"):
    if not text_input.strip():
        st.warning("Please enter some recipe text first.")
    else:
        with st.spinner("Extracting recipe..."):
            recipe = extract_recipe(text_input)
            st.session_state["recipe"] = recipe

if "recipe" in st.session_state:
        recipe = st.session_state["recipe"]
 
        st.subheader(recipe.recipe_name)
        if recipe.prep_time_minutes:
            st.markdown(f"**Prep time:** {recipe.prep_time_minutes} minutes")
 
        st.markdown("### Ingredients")
        for ingredient in recipe.ingredients:
            st.write(f"- {ingredient.quantity} {ingredient.name}")
 
        st.markdown("### Instructions")
        for i, step in enumerate(recipe.instructions, start=1):
            st.write(f"{i}. {step}")
