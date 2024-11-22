document.addEventListener('DOMContentLoaded', (event) => {
    fetch('/tiny')
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed: Network Errors')
            }
            return response.json();
        })
        .then(data => {
            const tiny = data.key
            if (!tiny) {
                throw new Error('API key not fetched');
            }

            // Construct the Script element
            let sc = document.createElement('script');
            sc.src = `https://cdn.tiny.cloud/1/${tiny}/tinymce/7/tinymce.min.js`
            sc.referrerPolicy = 'origin';
            // Initialize the Script
            sc.onload = () => {
                tinymce.init({
                    selector: 'textarea#id_content',
                    plugins: [
                        'advlist', 'autolink', 'link', 'image', 'lists', 'charmap', 'preview', 'anchor', 'pagebreak',
                        'searchreplace', 'wordcount', 'visualblocks', 'visualchars', 'code', 'fullscreen', 'insertdatetime',
                        'media', 'table', 'emoticons', 'help'
                    ],
                    toolbar: 'undo redo | styles | bold italic | alignleft aligncenter alignright alignjustify | ' +
                    'bullist numlist outdent indent | link image | print preview media fullscreen | ' +
                    'forecolor backcolor emoticons | help',
                })
            }
            // Insert the Script in the Head Tag
            document.head.appendChild(sc);
        })
        // Errors arising from fetching the Key
        .catch(error => {
            console.error('Error fetching the Tiny Key:', error);
        });
})