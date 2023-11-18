
// navBar
let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
    menu.classList.toggle('bx-x')
    navbar.classList.toggle('open');
    
    
}

// document.addEventListener('DOMContentLoaded', function () {
//     var header = document.querySelector('header');
//     var lastScrollTop = 0;

//     window.addEventListener('scroll', function () {
//         var currentScrollTop = window.scrollY;

//         if (currentScrollTop > lastScrollTop) {
//             // Scrolling down
//             header.classList.add('dark-background');
//         } else {
//             // Scrolling up
//             header.classList.remove('dark-background');
//         }

//         lastScrollTop = currentScrollTop;
//     });
// });

document.addEventListener('DOMContentLoaded', function () {
    var header = document.querySelector('header');
    var lastScrollTop = 0;
    var delta = 7; // Adjust this value based on your needs

    window.addEventListener('scroll', function () {
        var currentScrollTop = window.scrollY;

        if (Math.abs(lastScrollTop - currentScrollTop) <= delta) {
            return;
        }

        if (currentScrollTop > lastScrollTop) {
            // Scrolling down
            header.style.top = '-' + header.offsetHeight + 'px';
        } else {
            // Scrolling up
            header.style.top = '0';
        }

        lastScrollTop = currentScrollTop;
    });
});
// end nav bar