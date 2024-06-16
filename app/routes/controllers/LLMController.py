from flask import jsonify
import json
import re
from openai import OpenAI, AssistantEventHandler
from ...config import main_config


def getPrompt():
    tinggi_badan = 97.5
    usia = 24
    status = 'stunted,overweight'
    berat_badan = 65
    jenis_kelamin = 'laki-laki'
    messages = getPromptLocally(
        tinggi_badan, usia, status, berat_badan, jenis_kelamin
    )
    return jsonify({'success': 'OK', 'message': str(messages)}), 200


def getPromptLocally(tinggi_badan, usia, status, berat_badan, jenis_kelamin):
    client = OpenAI(api_key=main_config['OPENAI_KEY'])
    # Create a new thread
    thread = client.beta.threads.create()
    input_message = 'tinggi badan: {}, usia: {} tahun, status_gizi:{}, berat badan:{}, jenis kelamin:{}'.format(
        tinggi_badan, usia , status, berat_badan, jenis_kelamin
    )

    message = client.beta.threads.messages.create(
        thread_id=thread.id, role='user', content=input_message
    )

    # Define the instructions for the assistant
    # instructions = 'Berikan rekomendasi makanan anak - anak berdasarkan input. tampilkan berupa list dan juga berikan rekomendasi penanganannya'
    assistant_id = 'asst_BZ2loRreVsga2g26VYYrSWAi'

    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant_id,
        # instructions=instructions,
    )

    messages = 'gagal membuat rekomendasi.'
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        messages = messages.data[0].content[0].text.value

    messages = re.sub(r'[*#]', '', messages)
    return str(messages)
