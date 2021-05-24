import React from 'react'
import styles from './Loader.module.scss'

export const Loader: React.FC = () => {
  return (
    <div className={styles.loader}>
      <div className={styles.bounce1} />
      <div className={styles.bounce2} />
    </div>
  )
}