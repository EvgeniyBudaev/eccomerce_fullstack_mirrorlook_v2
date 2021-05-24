import React from 'react'
import CatalogContent from './CatalogContent'
import styles from './CatalogPage.module.scss'

export const CatalogPage = () => {
  return (
    <section className={styles.catalog}>
      <div className={styles.container}>
        {/*<CatalogTop />*/}
        <div className={styles.inner}>
          {/*<CatalogAside />*/}
          <CatalogContent />
        </div>
      </div>
    </section>
  )
}