import React from 'react'
import styles from './button.module.scss'

const Button = (props) => {
  const {type, text, onClick, disabled} = props
  return <button
      type={type}
      className={styles.button}
      onClick={onClick}
      disabled={disabled}
  >
    {text}
  </button>
}

export default Button
