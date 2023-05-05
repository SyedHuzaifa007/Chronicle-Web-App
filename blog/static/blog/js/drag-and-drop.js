// Drag and drop file upload functionality
const link = document.querySelector('.article-title');
const colors = ['#dabbcd', '#5c5c5c', '#007acc']; // Add your colors here
let index = 0;

link.addEventListener('mouseenter', () => {
  link.style.color = colors[index];
  index = (index + 1) % colors.length;
});

link.addEventListener('mouseleave', () => {
  link.style.color = '';
});
function fileContainerChangeFile(e,element,id) {
	element.parentElement.classList.remove('fileContainerDragOver');
	try {
		element.previousElementSibling.getElementsByClassName('fileName')[0].textContent = "Done! It's added.";
		document.getElementById(id).checked = false;
	} catch (error) {}
	try {
		aName = element.value;
		if (aName !== '') {
		}
	} catch (error) {}
}

function fileContainerReplaceFile(e,element,id) {
	document.element.parentElement.classList.remove('fileContainerDragOver');
	try {
		element.previousElementSibling.getElementsByClassName('fileName')[0].textContent = 'Done! The file is replaced!';
		document.getElementById('removeImageContainer').classList.remove('removeImageContainer');
		document.getElementById('image_preview').style.opacity=0.1;
		document.getElementById('image_preview').style.cursor='default';
		document.getElementById(id).checked = false;
	} catch (error) {}
	try {
		aName = element.value;
		if (aName !== '') {
		}
	} catch (error) {}
}

function onDrop(e,element) {
	element.classList.remove('fileContainerDragOver');
	try {
		element.getElementsByClassName('fileName')[0].style.display = "inline-block";
		element.getElementsByClassName('fileNameDrop')[0].style.display = "none";
	} catch (error) {}
}

function dragOver(e,element) {
	element.classList.add('fileContainerDragOver');
	element.getElementsByClassName('fileName')[0].style.display = "none";
	element.getElementsByClassName('fileNameDrop')[0].style.display = "inline-block";
	e.preventDefault();
	e.stopPropagation();
}

function leaveDrop(element) {
	element.classList.remove('fileContainerDragOver');
	element.getElementsByClassName('fileName')[0].style.display = "inline-block";
	element.getElementsByClassName('fileNameDrop')[0].style.display = "none";
}
