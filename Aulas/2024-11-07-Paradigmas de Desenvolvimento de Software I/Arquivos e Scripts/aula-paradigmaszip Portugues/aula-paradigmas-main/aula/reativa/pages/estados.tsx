import styles from "../styles/Home.module.css"; // Importa os estilos CSS
import { useEffect, useState } from "react";

function ContadorComMensagem() {
  const [contador, setContador] = useState(0)

  useEffect(()=>{
    const d = new Date();
    let time = d.getTime();
    console.log(`o contador mudou para: ${contador}`, time)
  },[contador] )

  const incremementar = () =>{
    const d = new Date();
    let time = d.getTime();
    setContador(contador + 1);
    console.log(contador,time); 
  };
  return (
  <main className={styles.main}>
    <p className={styles.aula}> Voce clicou {contador} vezes </p>
    <button onClick={incremementar}>Incrementar</button>
  </main>
  );

}

export default ContadorComMensagem;
