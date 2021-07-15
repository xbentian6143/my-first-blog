function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// $(document).ready(f) ≒ window.addEventListener("load", f)

function sympathy1(event, post_pk,sympathys_count) {
  console.log(post_pk)
  
      fetch("http://127.0.0.1:8000/sympathy1/" +post_pk+ "/" +sympathys_count+ "/", {
              method: 'POST',
              headers: {
                  "Content-Type": "application/json; charset=utf-8",
                  "X-CSRFToken": getCookie("csrftoken"),
              },
          body: JSON.stringify({"status": "requested by javascript."})
          }
      )
      .then(response => response.json())
      .then(json => {
          // json-value
          console.log(json)
          console.log(`.post-${json.post_pk}`)
          const container = document.querySelector(`.post-${json.post_pk}`);
          if (json.liked == true) {
            container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/> </svg> ${json.sympathys_count}`;
          } else {
            container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16"><path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/></svg>  ${json.sympathys_count}`;
          }
      
         
      })


}

function sympathy2(event, post_pk,sympathys_count) {
  console.log(post_pk)
  
      fetch("http://127.0.0.1:8000/sympathy2/" +post_pk+ "/" +sympathys_count+ "/", {
              method: 'POST',
              headers: {
                  "Content-Type": "application/json; charset=utf-8",
                  "X-CSRFToken": getCookie("csrftoken"),
              },
          body: JSON.stringify({"status": "requested by javascript."})
          }
      )
      .then(response => response.json())
      .then(json => {
          // json-value
          console.log(json)
          console.log(`.post-${json.post_pk}`)
          const container = document.querySelector(`.post-${json.post_pk}`);
          if (json.liked == true) {
            container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/> </svg>  ${json.sympathys_count}`;
          } else {
            container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16"><path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/></svg> ${json.sympathys_count}`;
          }
      
         
      })


}



function good1(event, idea_pk,goods_count) {
    console.log(idea_pk)
    
        fetch("http://127.0.0.1:8000/good1/" +idea_pk+ "/" +goods_count+ "/", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            body: JSON.stringify({"status": "requested by javascript."})
            }
        )
        .then(response => response.json())
        .then(json => {
            // json-value
            console.log(json)
            console.log(`.idea-${json.idea_pk}`)
            const container = document.querySelector(`.idea-${json.idea_pk}`);
            if (json.liked == true) {
              container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/> </svg>  ${json.goods_count}`;
            } else {
              container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16"><path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/></svg>  ${json.goods_count}`;
            }
        
           
        })


}

function good2(event, idea_pk,goods_count) {
    console.log(idea_pk)
    
        fetch("http://127.0.0.1:8000/good2/" +idea_pk+ "/" +goods_count+ "/", {
                method: 'POST',
                headers: {
                    "Content-Type": "application/json; charset=utf-8",
                    "X-CSRFToken": getCookie("csrftoken"),
                },
            body: JSON.stringify({"status": "requested by javascript."})
            }
        )
        .then(response => response.json())
        .then(json => {
            // json-value
            console.log(json)
            console.log(`.idea-${json.idea_pk}`)
            const container = document.querySelector(`.idea-${json.idea_pk}`);
            if (json.liked == true) {
              container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart-fill" viewBox="0 0 16 16"><path fill-rule="evenodd" d="M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314z"/> </svg> ${json.goods_count}`;
            } else {
              container.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-heart" viewBox="0 0 16 16"><path d="m8 2.748-.717-.737C5.6.281 2.514.878 1.4 3.053c-.523 1.023-.641 2.5.314 4.385.92 1.815 2.834 3.989 6.286 6.357 3.452-2.368 5.365-4.542 6.286-6.357.955-1.886.838-3.362.314-4.385C13.486.878 10.4.28 8.717 2.01L8 2.748zM8 15C-7.333 4.868 3.279-3.04 7.824 1.143c.06.055.119.112.176.171a3.12 3.12 0 0 1 .176-.17C12.72-3.042 23.333 4.867 8 15z"/></svg>  ${json.goods_count}`;
            }
        
           
        })


}



/*        
window.addEventListener("load", () => {
    // document.querySelector: CSSセレクタで要素を取得
    // Element#addEventListener: onみたいなやつ
    // 関数内でawaitを使うならasyncをつける必要あり
    // goodは複数あるんだよね？だったらクラスセレクタを使わないといけない
    document.querySelector("#good").addEventListener("click", async (event) => {
      event.preventDefault();
      console.log("HELLO");
      
      const response = await fetch("http://127.0.0.1:8000/good/", {
        method: "POST",
        headers: {
          // 送るデータがJSONであることを明示する必要がある
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({
          "idea_pk":8,
        }),
      });
      const json = await response.json();
      // getElementByNameは使えないと思う（フォーム要素のみ）
      const container = document.querySelector(`.${response.idea_pk}`);
      if (json.liked) {
        container.innerHTML = 'できた';
      } else {
        container.innerHTML = 'できたお';
      }
    });
});

*/
