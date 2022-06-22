
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize(text: str, per: float):
    text = text.replace('\n\n', ' ')
    text = text.replace('.', '.<eos>')
    text = text.replace('?', '?<eos>')
    text = text.replace('!', '!<eos>')
    sentences = text.split('<eos>')
    current_chunk = 0
    max_chunk = 500 
    chunks = []
    for sentence in sentences:
        if len(chunks) == current_chunk + 1: 
            if len(chunks[current_chunk]) + len(sentence.split(' ')) <= max_chunk:
                chunks[current_chunk].extend(sentence.split(' '))
            else:
                current_chunk += 1
                chunks.append(sentence.split(' '))
        else:
            print(current_chunk)
            chunks.append(sentence.split(' '))

    for chunk_id in range(len(chunks)):
        chunks[chunk_id] = ' '.join(chunks[chunk_id])
    Len = len(text.split())
    res = summarizer(chunks, min_length=int(Len*(per-0.05)/len(chunks)), max_length=int(Len*(per+0.05)/len(chunks)))
    sum = '\n\n'.join([summ['summary_text'] for summ in res])
    return sum
