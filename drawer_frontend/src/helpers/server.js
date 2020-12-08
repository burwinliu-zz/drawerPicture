

export const getImage = async () => {
    const response = await fetch('http://127.0.0.1:5000/get_image');
    const images = await response.blob();
    return URL.createObjectURL(images);
}



export const getLabels = async () => {
    const response = await fetch('http://127.0.0.1:5000/get_labels');
    const labels = await response.json();
    console.log("retrieved ", labels)
    return labels['labels'];
}

export const addLabels = (label) => {
    fetch('http://127.0.0.1:5000/add_labels?label=' + label);
    return;
}