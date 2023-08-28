

const consonantRegex = /[bcdfghjklmnpqrstvwxyz]/i;

class PlaceholderInitialsAvatar {
    // My first thought was to create class that will describe object which takes name
    // and then produces an initials and renders html with them inside
    // but I've changed my mind since in my case this.name will be stored elsewhere 
    // efectivelly making having this class useless.
    // So it will function better as some kind of namespace with functions that are able 
    // to produce initials and render corresponding avatar


    // constructor(name) {
    //     this.name = name;
    // }

    static initials(name){
        var letters = [name[0]];
        for (const char of name) {
            if (consonantRegex.test(char)) {
                letters.push(char);
                break;
            }
        }
        return letters.join("").toUpperCase();  
    }
        
    // get initials(){
    //     return this._initials(this.name);
    // }

    static render(name){

        var initials = PlaceholderInitialsAvatar.initials(name);
        // create and style span
        var span = document.createElement("span");
        span.classList.add(
            ...`font-medium text-gray-600`.split(" ")
        );
        span.textContent = initials;

        var container_div = document.createElement("div");
        container_div.classList.add(
            ...`relative inline-flex items-center 
            justify-center w-10 h-10 overflow-hidden 
            bg-indigo-300 rounded-full`.split("\n").map((a) =>{return a.trim()}).join(" ").split(" ")
        );

        container_div.appendChild(span);
        return container_div;
    }

    // render(){
    //     return this._render(this.initials)
    // }
}

export default PlaceholderInitialsAvatar;