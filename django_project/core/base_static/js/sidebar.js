const toggleSidebar = () => {
    /*
   const sidebar = document.getElementById('sidebar')
   sidebar.classList.toggle('active')
   */
    $('#sidebar').toggle();
}

$(document).ready(function () {

        $('#sidebarCollapse').on('click', function () {
            // $('#sidebar').toggleClass('active');
            toggleSidebar();
        });

});
