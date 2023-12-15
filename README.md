# Fake News Detector

## Overview
The Fake News Detector is a machine learning-based application designed to identify and classify news related to climate change as real or fake. It utilizes advanced natural language processing techniques and deep learning models to analyze text and provide insights.

## Features
- **Text Analysis**: Processes and classifies text data to determine the authenticity of news.
- **Image Processing**: Includes an OCR (Optical Character Recognition) feature to extract text from images for analysis.
- **API Integration**: Offers a Flask API for easy integration and interaction with the model.
- **Scraping Tools**: Contains scripts for scraping news data from specified sources.

## Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**
   ```
   git clone https://github.com/AMustafa4983/Fake_news_detector.git
   cd Fake_news_detector
   ```

2. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```
   python api.py
   ```

## Usage

The application can be used in two ways:

1. **Text Analysis**
   - Send a POST request to `/predict` with a JSON payload containing the text to be analyzed.

2. **Image Analysis**
   - Send a POST request to `/predict-image` with an image file. The text will be extracted and analyzed.

## Contributing

Contributions to improve the accuracy and efficiency of the Fake News Detector are welcome. Please follow the standard fork-and-pull request workflow for contributions.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

This project is open-sourced under the MIT License. See the [LICENSE](LICENSE) file for more details.
