document.addEventListener('DOMContentLoaded', function () {
    const modal = document.getElementById('syllabus-modal');
    const closeBtn = document.getElementById('close-btn');
    const loading = document.getElementById('loading');

    // Add event listener to the form for generating syllabus
    document.getElementById('syllabus-form').addEventListener('submit', async function (event) {
        event.preventDefault();

        // Show loading animation
        loading.style.display = 'block';

        // Prepare form data
        const formData = new FormData(this);

        try {
            // Send POST request to server to generate syllabus
            const response = await fetch('/generate_syllabus', {
                method: 'POST',
                body: formData
            });

            // Parse JSON response
            const result = await response.json();

            // Generate HTML for displaying syllabus
            let syllabusHtml = `<h2>${result.title}</h2>`;
            syllabusHtml += `<p><strong>Description:</strong> ${result.description}</p>`;
            result.sections.forEach(section => {
                syllabusHtml += `<h3>${section.title}</h3><p>${section.content.replace(/\n/g, '<br>')}</p>`;
            });

            // Display generated syllabus in modal
            const aiResponse = document.querySelector('.ai-response');
            aiResponse.innerHTML = syllabusHtml;
            modal.style.display = 'block'; // Show modal with syllabus content

        } catch (error) {
            console.error('Error fetching or parsing data:', error);
            // Optionally handle errors, e.g., display error message
        } finally {
            // Hide loading animation after processing
            loading.style.display = 'none';
        }
    });

    // Event listener for closing the modal
    closeBtn.addEventListener('click', function () {
        modal.style.display = 'none'; // Hide modal on close button click
    });

    // Close modal if user clicks outside the modal content
    window.addEventListener('click', function (event) {
        if (event.target === modal) {
            modal.style.display = 'none';
        }
    });
});
