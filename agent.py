from nearai.agents.environment import Environment


def run(env: Environment):
    # Your agent code here
    prompt = {
        "role": "system",
        "content": "Extract the product name from the user query and generate a structured response with a primary search link followed by three feature-enhanced variations. Ensure that only the main product search link is bolded, while the feature links remain plain text. Format the output as follows:    **Output Format:** **DONT SAY ANYTHING ELSE BEFORE THIS Click to view a collection of PRODUCT NAME sorted from low to high prices: <br /> 🔍 [The cheapest PRODUCT_NAME](https://www.google.com/search?q=PRODUCT_NAME&udm=28&shoprs=CAEYFyoQZWxlY3RyaWMgc2Nvb3RlcjIcCBcSElByaWNlOiBsb3cgdG8gaGlnaCoEEAEYAWACiAEB&sa=X&ved=2ahUKEwih9N74tIuMAxVdCjQIHR3UJ9sQ268JKAB6BAgUEAw&biw=1400&bih=865&dpr=1.8)**    - (appropriate emoji here) [FEATURE_1](https://www.google.com/search?q=PRODUCT_NAME+FEATURE_1&udm=28&shoprs=CAEYFyoQZWxlY3RyaWMgc2Nvb3RlcjIcCBcSElByaWNlOiBsb3cgdG8gaGlnaCoEEAEYAWACiAEB&sa=X&ved=2ahUKEwih9N74tIuMAxVdCjQIHR3UJ9sQ268JKAB6BAgUEAw&biw=1400&bih=865&dpr=1.8)   - (appropriate emoji here) [FEATURE_2](https://www.google.com/search?q=PRODUCT_NAME+FEATURE_2&udm=28&shoprs=CAEYFyoQZWxlY3RyaWMgc2Nvb3RlcjIcCBcSElByaWNlOiBsb3cgdG8gaGlnaCoEEAEYAWACiAEB&sa=X&ved=2ahUKEwih9N74tIuMAxVdCjQIHR3UJ9sQ268JKAB6BAgUEAw&biw=1400&bih=865&dpr=1.8)   - (appropriate emoji here) [FEATURE_3](https://www.google.com/search?q=PRODUCT_NAME+FEATURE_3&udm=28&shoprs=CAEYFyoQZWxlY3RyaWMgc2Nvb3RlcjIcCBcSElByaWNlOiBsb3cgdG8gaGlnaCoEEAEYAWACiAEB&sa=X&ved=2ahUKEwih9N74tIuMAxVdCjQIHR3UJ9sQ268JKAB6BAgUEAw&biw=1400&bih=865&dpr=1.8)  **Rules:**  - Always render markdown DO NOT return markdown with messy search URL in closed brackets it must be rendered markdown.  - Replace spaces with `+` in URLs.   - Ensure that only the first product search link is bolded, while the feature links remain plain text.   - If no product is identified, return **'No product found.''",
    }
    result = env.completion([prompt] + env.list_messages())
    env.add_reply(result)
    env.request_user_input()


run(env)
