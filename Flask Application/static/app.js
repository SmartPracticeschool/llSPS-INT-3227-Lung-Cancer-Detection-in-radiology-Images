const fileSelector = document.getElementById('filechoose');
const imagepreview = document.querySelector('img');
const upload_image_paragaph = document.getElementById("upload-image-text");
const submitButton = document.getElementById('file-submit');
const resultdiv = document.getElementById('result');

let SelectedFile = null;

fileSelector.addEventListener('change', (event) => {
    // After the File is Selected
    const file = event.target.files && event.target.files[0];
    const reader = new FileReader();

    reader.onload = (event) => {
        imagepreview.src = event.target.result;
        SelectedFile = file;
        imagepreview.style.display = 'inline-block'
        upload_image_paragaph.style.display = 'none'
    }

    if(file){
        reader.readAsDataURL(file);
    }else{
        SelectedFile = null
    }
});

submitButton.addEventListener('click' , async (event) => {
    if(SelectedFile){
        // File is Present
        const form_data = new FormData();
        form_data.append('image',SelectedFile);
        axios.post('http://127.0.0.1:5000/upload',form_data,{
            headers: {
                'Content-Type': 'multipart/form-data'
              }
        }).then(({data}) => {
            // responser from the Sever.
            resultdiv.classList.add('active');
            resultdiv.classList.remove('normal','affected');
            resultdiv.classList.add(data == 'Normal' ? 'normal' : 'affected');
            resultdiv.innerHTML = `<p>${data}</p>`
        }).catch(err => {
            console.log(err);
        })
    
    }else{
        alert('kindly Select the File');
    }
})

