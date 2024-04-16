const card_content = document.querySelectorAll(
    ".demo-card-square.mdl-card.mdl-shadow--2dp.col-md-3.no-padding"
);
let list_object = [];

card_content.forEach(div_content => {
    let span = div_content.querySelector('span.mdl-card__stock');
    let spanExist = span.textContent.trim().replace(/\s+/g, ""); // Elimina los espacios en blanco que haya
    const matches = spanExist.match(/EXIS(\d+)/); // Busca la palabra EXIS seguida de un número
    let product_object = {
        code: "",
        cp: "",
        description: "",
        existence: 0,
        price: 0,
        obtained_from: "cva"
    };
    if (matches) {
        if (parseInt(matches[1]) > 0) {
            let text_complete = div_content.querySelectorAll(
                ".mdl-card__supporting-text.is-height-desc.d-inline-flex.justify-content-md-center.align-items-center"
            );
            let cp = div_content.querySelector('.mdl-card__title-text');
            let price = div_content.querySelector('.mdl-card__legend-promo-price.d-inline-flex.justify-content-md-center.align-items-center').innerText.split('\n')[1].split(' ')[0];
            //if (text_complete && text_complete.length > 0) {
            let comp = text_complete[0].innerText;
            let parts = comp.split('\n');
            product_object.code = parts[0].split(':')[1].trim();
            product_object.description = parts[1].trim(); 
            //}
            product_object.cp = cp.textContent.trim();
            product_object.price = parseFloat(price);
            product_object.existence = parseInt(matches[1]);

            list_object.push(product_object);
        }
    }
});