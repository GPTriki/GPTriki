const stream = document.querySelector('video').srcObject;
const recorder = new MediaRecorder(stream);

const chunks = [];

recorder.addEventListener('dataavailable', event => chunks.push(event.data));
recorder.start();

function save() {
    recorder.requestData()
    const blob = new Blob(chunks, { type: recorder.mimeType });
    const downloadUrl = URL.createObjectURL(blob);

    const link = document.createElement('a');
    link.href = downloadUrl;
    link.download = 'media.mkv';

    document.body.appendChild(link);
    link.click();

    URL.revokeObjectURL(downloadUrl);
    document.body.removeChild(link);
    chunks = [];
}
