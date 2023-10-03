var block_user = document.getElementById('user');
var block_data_client = document.getElementById('cliente');
var block_data_client_paga = document.getElementById('forma-pago');
var btn_next = document.getElementById('next');
var btn_prev = document.getElementById('prev');
var btn_submit = document.getElementById('submit');
var page = 0;

function next_page() {
    block_data_client.style = 'display:none';
    block_user.style = 'display:none';
    block_data_client_paga.style = 'display:none';
    btn_prev.style = 'display:none';
    btn_next.style = 'display:none';
    btn_submit.style = 'display:none';
    if (page < 2)
        page++;
    else
        page = 1;
    switch (page) {
        case 1:
            block_data_client.style = '';
            btn_next.style = '';
            btn_prev.style = '';
            break;
        case 2:
            block_data_client_paga.style = '';
            btn_prev.style = '';
            btn_submit.style = '';
            break;
        default:
            block_user.style = '';
            btn_next.style = '';
            break;
    }
}

function prev_page() {
    block_data_client.style = 'display:none';
    block_user.style = 'display:none';
    block_data_client_paga.style = 'display:none';
    btn_prev.style = 'display:none';
    btn_next.style = 'display:none';
    btn_submit.style = 'display:none';
    if (page > 0)
        page--;
    else
        page = 0;
    switch (page) { 
        case 0:
            block_user.style = '';
            btn_next.style = '';
            break;
        case 1:
            block_data_client.style = '';
            btn_prev.style = '';
            btn_next.style = '';
            break;
        default:
            block_data_client_paga.style = '';
            btn_prev.style = '';
            btn_submit.style = '';
            break;
    }
}
