import React from 'react'
import styles from './FooterLogoAndSocial.module.scss'
import FooterLogo from './FooterLogo'
import Facebook from './Facebook'
import Vk from './Vk'
import Instagram from './Instagram'
import Twitter from './Twitter'

export const FooterLogoAndSocial: React.FC = () => {
  return (
    <>
      <div className={styles.footerLogo}>
        <FooterLogo />
      </div>
      <div className={styles.socialIcons}>
        <div className={styles.socialIcon}>
          <Facebook />
        </div>
        <div className={styles.socialIcon}>
          <Vk />
        </div>
        <div className={styles.socialIcon}>
          <Instagram />
        </div>
        <div className={styles.socialIcon}>
          <Twitter />
        </div>
      </div>
    </>
  )
}