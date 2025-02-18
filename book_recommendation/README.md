# Hybrid-Book-Recommendation-System

This project is part of the 6th semester Big Data Analytics (BDA) coursework and focuses on two main tasks: Hybrid Recommendation System and Association Rules Mining.

## Dataset

The project utilizes a book dataset sourced from Kaggle, which can be accessed from my GitHub repository [Github Link](https://github.com/AllahRakha1234/Datasets/tree/master) or directly from Kaggle using the following link: [Best Book Ever Data for 2021](https://www.kaggle.com/datasets/shashwatwork/best-book-ever-data-for-2021).

## Tools Used

- **Frontend:** Streamlit
- **Backend:** Python with libraries such as Pandas, NumPy, and scikit-learn

## Usage Instructions

To use this project:

1. Run the **Hybrid_Rec_System.ipynb** file in a Colab/Kaggle environment.
2. Download the required dataset file from Kaggle.
3. The notebook will generate pickle files which are used in subsequent steps.
4. Adjust paths in the **data_upload.py** file as needed.
5. Run **data_upload.py** to prepare the data.
6. Run **app.py** to execute the application.

## Requirements

Install the required packages using:
```bash
pip install -r requirements.txt
```

## How to Run

Start the Streamlit server by running:
```bash
streamlit run app.py
```

## How to Start the App

To start the application, follow these steps:

1. Ensure all required packages are installed by running:
    ```bash
    pip install -r requirements.txt
    ```
2. Prepare the data by running:
    ```bash
    python data_upload.py
    ```
3. Start the Streamlit server by running:
    ```bash
    streamlit run app.py
    ```

## Demo

A demo video and presentation slides (PPT) are available in the repository. You can also access the project report for more details.
