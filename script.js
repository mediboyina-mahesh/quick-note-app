async function saveNote() {

    let note = document.getElementById("note").value;

    await fetch("/save-note", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            note: note
        })
    });

    document.getElementById("note").value = "";

    loadNotes();
}

async function loadNotes() {

    let response = await fetch("/notes");

    let notes = await response.json();

    let list = document.getElementById("notesList");

    list.innerHTML = "";

    notes.forEach(item => {

        let li = document.createElement("li");

        li.innerText = item[0];

        list.appendChild(li);
    });
}

loadNotes();