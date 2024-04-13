function changeForm(event, form_id) {

    const button = document.querySelectorAll('.button');
    button.forEach(b => {
        b.classList.remove('active')
    })
    document.querySelector('.active_form').classList.remove('active_form')
    document.getElementById(form_id).className = 'active_form';
    event.currentTarget.classList.add('active')

}
