import React from 'react'
import Header from "../../Header"
import Footer from '../../Footer'
import styles from './MainLayout.module.scss'

export const MainLayout: React.FC = (props) => {
  return (
        <>
      <div className={styles.wrapper}>
        <div className={styles.content}>
          <Header />
          {props.children}
        </div>
        <div className={styles.footer}>
          <Footer />
        </div>
      </div>
    </>
  )
}