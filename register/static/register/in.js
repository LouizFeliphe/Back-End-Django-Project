let span = document.querySelectorAll(".helptext");
let label = document.getElementsByTagName("label")


let label1 = label[0]
label1.innerHTML = "Nome de usuário:"

let label2 = label[2]
label2.innerHTML = "Senha:"

let label3 = label[3]
label3.innerHTML = "Confirmação de senha:"


let span1 = span[0]
span1.innerHTML = "Nome de usuário requisitado. 150 caracteres ou menos."

let span2 = span[1]
span2.innerHTML = "<ul><li>Sua senha não pode ser muito similar a sua outra informação pessoal.</li><li>Sua senha deve conter pelo menos 8 caracteres.</li><li>Sua senha não pode ser uma senha frequentemente usada.</li><li>Sua senha não pode ser inteiramente numérica.</li></ul>"

let span3 = span[2]
span3.innerHTML = "Insira a mesma senha de antes, para verificação."