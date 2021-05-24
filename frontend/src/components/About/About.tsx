import React from 'react'
import AboutLeft from './AboutLeft'
import styles from './About.module.scss'

export  const About: React.FC = () => {
  return (
    <section className={styles.about}>
      <div className={styles.container}>
        <div className={styles.inner}>
          <AboutLeft />
        </div>
      </div>
    </section>
  )
}