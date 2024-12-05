import { useEffect, useState } from "react";
import styles from "../styles/Home.module.css"; // Importa os estilos CSS

function ListaDeUsuarios() {
  const[usuarios,  setUsuarios] = useState([]);
  const[carregando,  setCarregando] = useState(true);

  useEffect(()=>{
    setTimeout(() => {fetch("https://jsonplaceholder.typicode.com/users")
      .then((response)=>response.json())
      .then((data)=>{
        setUsuarios(data);
        setCarregando(false);
      })
      
    }, 1000);
    
      ;
  },[]  ) //[] significa que o efeito roda apenas ao montar o componente
  
  if(carregando)
  {
    return <p>Loading ... </p>
  }

  return (
    <main className={styles.main}>
      <h1 className={styles.aula}>Lista de Usuários</h1>
      <ul className={styles.aula}>
        {usuarios.map((usuario)=>(
          <li key={usuario.id}> {usuario.name}</li>
        ))}
      </ul>
    </main>
  );
}

export default ListaDeUsuarios;
