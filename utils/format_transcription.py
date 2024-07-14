from models.google_gemini import get_response

def format_transcription(transcriptions):
    formatted_transcriptions = []
    for start, transcription in transcriptions:
        prompt = f""" 
        Format the transcription with accurate line breaks and full stops:
        {transcription}
        """
        response = get_response(prompt)
        formatted_transcriptions.append((start, response))
    return formatted_transcriptions