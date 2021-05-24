import React from 'react'
import { Route, Switch } from 'react-router-dom'
import MainLayout from "../Layouts/MainLayout"
import {ROUTES} from '../../routes'
import AboutPage from '../About'
import CatalogPage from "../Pages/CatalogPage"

export const App = () => {
    return (
        <MainLayout>
            <Switch>
                <Route path={ROUTES.ABOUT} component={AboutPage} />
                <Route path={ROUTES.CATALOG + ':catalogSlug/'} component={CatalogPage} exact />
            </Switch>
        </MainLayout>
    )
}