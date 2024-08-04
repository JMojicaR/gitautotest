'use strict'

async function inputUser() {
    return $('div.container>input[type=text]')
}

async function inputPassword() {
    return $('div.container>input[type=password]')
}

async function buttonLogin() {
    return $('div.container>button[type=submit]')
}

async function buttonCancel() {
    return $('div.container>button[type=submit]')
}