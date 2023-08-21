# Flipify Chatbot

Flipify is a chatbot designed to provide users with fashion suggestions, product combinations, and fashion-related products available on Flipkart. This README provides an overview of the Flipify Chatbot project, its features, setup instructions, and usage guidelines.

## Features

Flipify comes equipped with the following features:

1. **Fashion Suggestions:** Flipify can provide users with personalized fashion suggestions based on their preferences, occasions, and style.

2. **Product Combinations:** The chatbot can offer creative combinations of fashion items to help users put together stylish outfits.

3. **Product Recommendations:** Flipify can recommend a variety of fashion products available on Flipkart, ranging from clothing and accessories to footwear.

4. **User Interaction:** The chatbot engages in natural language conversations, allowing users to interact with it in a human-like manner.

5. **User Profiles:** Users can create profiles to save their preferences and receive more accurate recommendations over time.

6. **Search and Browse:** Users can search for specific fashion items or browse through different categories of products available on Flipkart.

## Installation and Setup

Follow these steps to set up Flipify on your local machine:

1. **Install Dependencies:** Navigate to the project directory and install the required dependencies using:
   ```
   cd FlipkartGrid5.0
   pip install -r requirements.txt
   ```

2. **Configuration:** create `.env` file and fill in your OpenAPI credentials `OPEN_AI_KEY=<Your OpenAI key>`. If you don't have API credentials, you can obtain them by signing up on the Openai platform.

3. **Run the Chatbot:** Execute the following command to start the Flipify chatbot:
   ```
   chainlit run app.py
   ```

4. **Access the Chatbot:** Open your preferred web browser and navigate to `http://localhost:8000` to interact with Flipify.

## Usage

Once the Flipify chatbot is up and running, you can start using its features:

1. **Fashion Suggestions:** Enter your style preferences, occasion, and other relevant details to receive personalized fashion suggestions.

2. **Product Combinations:** Ask the chatbot for outfit ideas or combinations of different fashion items.

3. **Product Recommendations:** Inquire about specific fashion products or ask for recommendations in a particular category.

4. **User Profiles:** Create a user profile to save your preferences and receive more accurate recommendations over time.

5. **Search and Browse:** Use natural language to search for fashion items or explore different product categories available on Flipkart.

## Contributing

We welcome contributions to the Flipify project! If you'd like to contribute new features, improvements, or bug fixes, please follow these steps:

1. Fork the repository and create a new branch for your contribution.
2. Make your changes and test thoroughly.
3. Submit a pull request, providing a detailed description of your changes.

## Support

If you encounter any issues or have questions about using Flipify, please feel free to [open an issue](https://github.com/abhinandansingla/flipify-chatbot/issues). We'll be happy to assist you!

## License

This project is licensed under the [MIT License](LICENSE).

---

Happy shopping and styling with Flipify! If you have any further questions or need assistance, don't hesitate to reach out.
