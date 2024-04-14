document.addEventListener('DOMContentLoaded', () => {
    function getCookie() {
        return document.cookie.split('; ').reduce((acc, item) => {
            const [name, value] = item.split('=')
            acc[name] = value
            return acc
        }, {})
    }

    const forms = document.querySelector('.tabs_forms');
    if (getCookie().tab) {
        forms.querySelector(`[data-tab=${getCookie().tab}]`).classList.add('active_form')
        document.querySelector(`[data-tab=${getCookie().tab}]`).classList.add('active')

    } else {
        forms.querySelector('.active_form').classList.remove('active_form')
        forms.querySelector(`[data-tab=${'car'}]`).classList.add('active_form')
    }
    const tabs = () => {

        const getActiveButtonName = () => { //получение значения data-tab активной кнопки
            return document.querySelector('.btn.active').dataset.tab
        }
        const setActiveForm = () => { //установка активной формы
            if (forms.querySelector('.active_form')) {
                forms.querySelector('.active_form').classList.remove('active_form')
            }
            forms.querySelector(`[data-tab=${getActiveButtonName()}]`).classList.add('active_form')
            document.cookie = `tab=${getActiveButtonName()}`;

        }
        document.querySelectorAll('.btn').forEach(button => {

            button.addEventListener('click', () => {
                document.querySelector('.btn.active').classList.remove('active');

                button.classList.add('active');
                setActiveForm(getActiveButtonName())
            })
        })
        document.querySelectorAll('.submit_form').forEach(submit => {
            submit.addEventListener('click', () => {


            })
        })
    }
    tabs()
})







