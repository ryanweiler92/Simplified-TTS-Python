# Dedicated Python environment for a versatile and user-friendly Text-to-Speech (TTS) system.

## Installation

To install the Text-to-Speech (TTS) system, follow these steps:

1. **Creating a Virtual Environment**

   This step involves setting up a virtual environment for the project. Run the following command:

   ```
   python -m venv tts_env
   ```

2. **Activating the Environment**

   Once the virtual environment is created, activate it using:

   ```
   .\tts_env\Scripts\activate
   ```

3. **Installing TTS & Other Dependencies**

   With the environment activated:

   ```
   pip install -r requirements.txt
   ```

## Testing

To verify that TTS & other requirements installed correctly run the following command:

```
python test.py
```

This will create an mp3 file in the root directory that you can play to verify that TTS is working.

## Commands

- `tts --list_models`: This command lists all available pre-trained models for TTS.

## Terms

Understanding the terminology is crucial for effectively using the TTS system:

- **Model**: In TTS, models refer to different configurations of text-to-speech synthesis, encompassing variations in voice, language, and the underlying technology.

- **Type/Language/Dataset/Model Hierarchy**:

  - **Type/**: The first parts of the model names (e.g., tts_models, vocoder_models, voice_conversion_models) indicate the type of model.

    - **tts_models**: These are used for direct text-to-speech synthesis.
    - **vocoder_models**: These models generate audio from mel-spectrograms and are often used in combination with tts_models.
    - **voice_conversion_models**: These models are designed for converting one voice into another.

  - **Language/**: This specifies the language or dataset used to train the model. For example, en for English, de for German, multilingual for models trained on datasets from multiple languages, etc.

  - **Dataset/**: Names like ljspeech, thorsten, vctk, etc., refer to the specific datasets or speakers used for training the model. These datasets might contain recordings from one speaker or multiple speakers, and each has its unique characteristics.

  - **Model**: The last part of the name refers to the specific TTS technology or architecture used, such as tacotron2, glow-tts, vits, etc. Each of these represents a different approach to synthesizing speech from text.
