document.addEventListener('DOMContentLoaded', () => {
    const history_back = document.querySelector('.history_back');
    history_back.addEventListener('click', () => {
        window.history.back()
    })
})