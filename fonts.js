const fontsGotham = [
    "tabular_gotham_medium.ttf",
    "tabular_gotham_book.ttf",
    "tabular_gotham_light.ttf",
    "tabular_gotham_extra_light.ttf",
    "tabular_gotham_thin.ttf",
];
const fontsClarity = [
    "ClarityCity-Black.ttf",
    "ClarityCity-ExtraBold.ttf",
    "ClarityCity-Bold.ttf",
    "ClarityCity-SemiBold.ttf",
    "ClarityCity-Medium.ttf",
    "ClarityCity-Regular.ttf",
    "ClarityCity-Light.ttf",
    "ClarityCity-ExtraLight.ttf",
    "ClarityCity-Thin.ttf"
];
const fontsClarityTabular = [
    "Tabular_ClarityCity-Black.ttf",
    "Tabular_ClarityCity-ExtraBold.ttf",
    "Tabular_ClarityCity-Bold.ttf",
    "Tabular_ClarityCity-SemiBold.ttf",
    "Tabular_ClarityCity-Medium.ttf",
    "Tabular_ClarityCity-Regular.ttf",
    "Tabular_ClarityCity-Light.ttf",
    "Tabular_ClarityCity-ExtraLight.ttf",
    "Tabular_ClarityCity-Thin.ttf"
];
const sizes = Array.from({ length: 40 }, (_, i) => i * 2 + 20);

const fontSelector = document.getElementById('select_font');
const sizeSelector = document.getElementById('select_size');
const textareas = document.getElementsByTagName('textarea');

const loadFonts = (fontArray, folder, containerId) => {
    const container = document.getElementById(containerId);
    fontArray.forEach(fontFile => {
        const fontName = fontFile.split('.')[0];
        const font = new FontFace(fontName, `url(${folder}/${fontFile})`);
        font.load().then(function (loaded_face) {
            document.fonts.add(loaded_face);
            console.log(`Font loaded: ${fontName}`);
            fontSelector.innerHTML += `<option value="${fontName}">${fontName}</option>`;
            const style = `font-family: ${fontName};`;
            container.innerHTML += `<p style="${style}">${fontName}</p>`;
        }).catch(function (error) {
            console.log(`Failed to load font: ${error}`);
        });
    });
};

// Load both Gotham and Clarity fonts
loadFonts(fontsGotham, 'Gotham', 'all_gotham_fonts');
loadFonts(fontsClarity, 'ClarityCity', 'all_clarity_fonts');
loadFonts(fontsClarityTabular, 'TabularClarityCity', 'all_mono_fonts');

// Populate size options
sizes.forEach(size => {
    sizeSelector.innerHTML += `<option value="${size}">${size}</option>`;
});

function update() {
    const selectedFont = fontSelector.options[fontSelector.selectedIndex].value;
    const selectedSize = sizeSelector.options[sizeSelector.selectedIndex].value;

    document.body.style.fontFamily = selectedFont;
    document.body.style.fontSize = `${selectedSize}px`;

    for (let i = 0; i < textareas.length; i++) {
        textareas[i].style.fontFamily = selectedFont;
        textareas[i].style.fontSize = `${selectedSize}px`;
    }
}

fontSelector.addEventListener('change', update);
sizeSelector.addEventListener('change', update);

window.onload = update;
