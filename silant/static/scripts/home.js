document.addEventListener('DOMContentLoaded', () => {
    function getCookie() {
        return document.cookie.split('; ').reduce((acc, item) => {
            const [name, value] = item.split('=');
            acc[name] = value;
            return acc;
        }, {})
    }

    const forms = document.querySelector('.tabs_forms');

    if (getCookie().tab) {

        forms.querySelector(`[data-tab=${getCookie().tab}]`).classList.add('active_form');
        document.querySelector(`[data-tab=${getCookie().tab}]`).classList.add('active');
    } else {

        forms.querySelector(`[data-tab=${'car'}]`).classList.add('active_form');
        document.querySelector(`[data-tab=${'car'}]`).classList.add('active');
    }

    const tabs = () => {

        const getActiveButtonName = () => {
            //получение значения data-tab активной кнопки
            return document.querySelector('.btn.active').dataset.tab;
        }
        const setActiveForm = () => {
            //установка активной формы
            if (forms.querySelector('.active_form')) {
                forms.querySelector('.active_form').classList.remove('active_form');
            }
            forms.querySelector(`[data-tab=${getActiveButtonName()}]`).classList.add('active_form');

            document.cookie = `tab=${getActiveButtonName()}`;

        }
        document.querySelectorAll('.btn').forEach(button => {

            button.addEventListener('click', () => {
                document.querySelector('.btn.active').classList.remove('active');

                button.classList.add('active');
                setActiveForm(getActiveButtonName());
            })
        })
        // нажите кнопки войти или выйти

    }

    tabs();
    // когда пользователь нажимает кпопку выход не с главной страницы
    // нужно удалить активный класс формы , иначе будет 2 формы
    if (document.querySelector('.form-non-auth')) {
        forms.querySelector('.active_form').classList.remove('active_form');
    }

    document.querySelector('.button-general').addEventListener('click', () => {
        forms.querySelector('.active_form').classList.remove('active_form');
        document.cookie = `tab=car`;
    })

   function prov(selectorFormClass, inputClass) {
       const selectorAll = document.querySelectorAll(`.${selectorFormClass}`)
       const input = document.querySelector(`.${inputClass}`)
       selectorAll.forEach(selector => {

       })
       selectorAll.forEach(selector => {
           selector.addEventListener('change', () => {
               if (selector.options !== 0){
                   input.disabled = false;
               }
               if (selector.options === 0){
                   input.disabled = true;
               }

           });
       });
   }

   // prov('car_form', 'input_car');

})







