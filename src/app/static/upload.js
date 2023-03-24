const form = document.querySelector('#upload-form');
const spinnerContainer = document.querySelector('#spinner-container');

form.addEventListener('submit', async (e) => {
  e.preventDefault();
  const formData = new FormData(e.target);

  spinnerContainer.style.display = 'flex';

  try {
    const response = await fetch('/audio_uploadfile', {
      method: 'POST',
      body: formData,
    });

    if (response.ok) {
      spinnerContainer.style.display = 'none';
      // Redirect to a success page
      console.lof('response', response)
      window.location.href = '/success';
    } else {
      throw new Error('Failed to upload file');
    }
  } catch (error) {
    console.error(error);
    spinnerContainer.style.display = 'none';
    // Show an error message
    alert('Failed to upload file');
  }
});
