'use strict';

let pupp = require('puppeteer');

(async() => {
    let browser = await pupp.launch();
    let page = await browser.newPage();
    await page.goto('https://github.com/LuckyPigeon/LuckyPigeon/blob/master/CONTRIBUTING.md');
    // let innerText = await page.evaluate(() => document.querySelector('.file-info'));
    let element = await page.$('.file-info');
    let innerText = await page.evaluate(element => element.textContent, element);
    var textArray = await innerText.split('\n');
    textArray = textArray.map((element) => {
        return element.trim();
    })
    .filter(element => element != '');
    console.log(textArray);
    await browser.close();
})();