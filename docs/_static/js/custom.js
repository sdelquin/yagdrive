document.addEventListener('DOMContentLoaded', run)

function run(event) {
    // When building documentation with "make dirhtml", generated tables DO NOT include
    // the class '.table'. This is a fix for that situation.
    const tables = document.getElementsByTagName('table')
    for (let table of tables) {
        table.classList.add('table')
    }
}
